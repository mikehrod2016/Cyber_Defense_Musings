const Resource = require("../models/Resource");

// Gets All Training Resources
exports.getResources = async (req, res) => {
  // TODO: Implement find to get all resources
  let allResourcesQuery = Resource.find().exec();
  // Return 200 status with success: true and data: your resources
  allResourcesQuery.then(function(resources){
    res.status(200);
    res.json({success: true, data: resources});
    //console.log(resources);
  });
  //return;
};

// Get Single Training Resource
exports.getSingleResource = async (req, res) => {
  try {
    // TODO: Implement findById and pass req.params.id
    let pickedResourceQuery = Resource.findById(req.params.id).exec();
    pickedResourceQuery.then(function(resource){
    // Return 200 status with success: true and data: your resource
    res.status(200);
    //console.log(req.params.id);
    res.json({success: true, data: resource});
    });
  } catch (err) {
    // TODO: Return 400 status with success: false, error: err.message
    res.status(400);
    res.json({success: false, error: err.message});
  }
  //return;
};

// Create Training Resource
exports.createResource = async (req, res) => {
  try {
    // TODO: Implement create and pass req.body
    let newResource = Resource.create(req.body);
    // Return 200 status with success: true and data: your resource
    res.json({success: true, data: newResource});
    return;
  } catch (err) {
    // TODO: Return 400 status with success: false, error: err.message
    res.status(400);
    res.json({success: false}, err.message);
    return;
  }
};

// Update Training Resource
exports.updateResource = async (req, res) => {
  try {
    // TODO: Implement findByIdAndUpdate and pass req.params.id & req.body
    Resource.findByIdAndUpdate(req.params.id, req.body);
    // Set to new record and run validators
    let updatedResource = Resource.findById(req.params.id);
    // Return 200 status with success: true and data: your resource
    res.status(200);
    res.json({success: true, data: updatedResource});
    return;
  } catch (err) {
    // TODO: Return 400 status with success: false, error: err.message
    res.status(400);
    res.json({success: false}, err.message);
    return;
  }
};

// Delete Training Resource
exports.deleteResource = async (req, res) => {
  try {
    // TODO: Implement findById and then use remove to delete the resource
    let deletionQuery = Resource.findByIdAndDelete(req.params.id).exec();
    // Return 200 status with success: true and data: empty
    deletionQuery.then(function(){
      res.status(200);
      res.json({success: true, data: 'empty'});
    });
    
  } catch (err) {
    // TODO: Return 400 status with success: false, error: err.message
    res.status(400);
    res.json({success: false, error: err.message});
    return;
  }
};
