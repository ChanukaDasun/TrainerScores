import { FileUploaderRegular } from "@uploadcare/react-uploader/next";
import "@uploadcare/react-uploader/core.css";
import { useState } from "react";
import { Button, message, Spin, Card, Typography } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import { uploadToUploadCare } from "./utils/uploadcareService";
import { readCertificates } from "./utils/certificateService";

const { Title, Text } = Typography;

export default function App() {
  const [certificate, setCertificate] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // handle file upload to Uploadcare
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    try {
      const cdnUrl = await uploadToUploadCare(file);
      setCertificate(cdnUrl);
      message.success("Image uploaded successfully!");
    } catch (error) {
      console.error(error);
      message.error("Failed to upload image.");
    } finally {
      setLoading(false);
    }
  };

  // send uploaded image CDN to FastAPI for processing
  const handleProcessCertificate = async () => {
    if (!certificate) {
      message.warning("Please upload a certificate first!");
      return;
    }

    setLoading(true);
    try {
      const response = await readCertificates(certificate);
      setResult(response);
      message.success("Certificate processed successfully!");
    } catch (error) {
      console.error(error);
      message.error("Error processing certificate.");
    } finally {
      setLoading(false);
    }
  };

  const getScoreColor = (score) => {
    if (score >= 8) return "#52c41a"; // green
    if (score >= 5) return "#faad14"; // orange
    return "#ff4d4f"; // red
  };

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", textAlign: "center" }}>
      <Card bordered style={{ padding: "24px", borderRadius: "12px" }}>
        <Title level={3}>Upload and Analyze Certificate</Title>
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          style={{ margin: "20px 0" }}
        />
        <br />
        {loading && <Spin size="large" />}
        {certificate && (
          <div style={{ margin: "20px 0" }}>
            <img
              src={certificate}
              alt="Uploaded certificate"
              style={{
                maxWidth: "100%",
                borderRadius: "8px",
                boxShadow: "0 0 8px rgba(0,0,0,0.1)",
              }}
            />
            <Text
              type="secondary"
              style={{ display: "block", marginTop: "8px" }}
            >
              CDN URL: {certificate}
            </Text>
          </div>
        )}
        <Button
          type="primary"
          icon={<UploadOutlined />}
          onClick={handleProcessCertificate}
          disabled={!certificate || loading}
        >
          Process Certificate
        </Button>
      </Card>

      {result && (
        <Card
          title="📄 Certificate Analysis Result"
          style={{
            marginTop: "24px",
            textAlign: "left",
            borderRadius: "12px",
            boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            background: "#fafafa",
          }}
        >
          <div style={{ marginBottom: "16px" }}>
            <Title level={4} style={{ marginBottom: 4 }}>
              Relevance Score:
            </Title>
            <Text
              strong
              style={{ fontSize: "1.5rem", color: getScoreColor(result.score) }}
            >
              {result.score?.toFixed(1) ?? "N/A"} / 10
            </Text>
          </div>

          <div>
            <Title level={4} style={{ marginBottom: 8 }}>
              Reasoning:
            </Title>
            <Text
              style={{
                whiteSpace: "pre-wrap",
                fontSize: "1rem",
                lineHeight: "1.6",
              }}
            >
              {result.reasoning || "No reasoning provided."}
            </Text>
          </div>
        </Card>
      )}
    </div>
  );
}
