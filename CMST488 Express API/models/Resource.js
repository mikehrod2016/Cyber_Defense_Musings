const mongoose = require("mongoose");

const ResourceSchema = new mongoose.Schema({
  name: {
    // TODO: string, required (provide a validation message), unique
    type: String, required: true, unique: true
  },
  provider: {
    // TODO: string, required (provide a validation message), unique
    type: String, required: true, unique: true
  },
  url: {
    // TODO: string, required (provide a validation message), unique
    type: String, required: true, unique: true
  }
});

module.exports = mongoose.model("Resource", ResourceSchema, 'resources');
