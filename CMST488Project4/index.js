const express = require("express");
const dotenv = require("dotenv");
const morgan = require("morgan");
const layouts = require("express-ejs-layouts");
const connectDB = require("./config/db");
const homeController = require("./controllers/homeController");
const resourceController = require("./controllers/ResourceController");

// Load env variables
dotenv.config({ path: "./config/config.env" });

// Init express app
const app = express();

// Init logging middleware
app.use(morgan("dev"));

// Connect to database
connectDB();

// Init EJS View Engine
app.set("view engine", "ejs");
app.use(layouts);

// Body Parser Middleware (Needed for post and put requests)
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Homepage Route
app.get("/", homeController.showIndex);

// Training Resources API Routes
app.get("/api/resources", resourceController.getResources);
app.get("/api/resources/:id", resourceController.getSingleResource);
app.post("/api/resources", resourceController.createResource);
app.put("/api/resources/:id", resourceController.updateResource);
app.delete("/api/resources/:id", resourceController.deleteResource);

// Init & Listen on defined port number
const PORT = 8000;
app.listen(PORT, () =>
  console.log(`Server started at http://localhost:${PORT}`)
);
