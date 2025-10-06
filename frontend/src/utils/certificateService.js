import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

const readCertificates = async (file_path) => {
  try {
    const response = await axios.post(`${BASE_URL}/certificate/score`, {
      "certificate_path": file_path
    });
    return response.data;
  } catch (error) {
    console.error("Error reading certificates:", error);
    throw error;
  }
};

export {
    readCertificates
};