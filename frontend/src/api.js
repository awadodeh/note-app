import axios from "axios";

export default axios.create({
  baseURL: `${process.env.DOMAIN}:${process.env.BACKEND_PORT}`
});
