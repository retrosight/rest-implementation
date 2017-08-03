# rest-implementation
A repository for the implementation of a REST API


## Install Brew and Node.js

```
brew update
brew install node
```

## Prepare the project folders and files

```
mkdir rest-implementation
cd rest-implementation
mkdir lib
touch lib/base.js index.js package.json
```

## Edit the source code

package.json

```json
{
  "name": "rest-implementation",
  "version": "1.0.0",
  "description": "A RESTful API.",
  "author": "https://github.com/retrosight/rest-implementation/graphs/contributors",
  "main": "index.js",
  "repository": "https://github.com/retrosight/rest-implementation",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {},
  "scripts": {
    "zip": "zip -r ../rest-implementation *"
  }
}
```

index.js

```javascript
var package = require("./package.json");
var base = require("./lib/base.js");
console.log("loaded " + package.name + ", version " + package.version);
exports.handler = function (event, context) {
  base.handleRequest(event, context.done);
}
```

lib/base.js

```javascript
exports.handleRequest = function (requestData, callback) {
  var responseData = {received_as_input: requestData};
  callback(null, responseData);
}
```

## Install and create zip archive

```
npm install
npm run zip
```

## Create the service in Lambda

Navigate to https://console.aws.amazon.com/lambda/home.

Click the **Get Started** Now button.

### Select blueprint

Click the **Blank Function** blueprint.

### Configure triggers

Select the **API Gateway** trigger by clicking the gray dashlined box.

```
API name:         rest-implementation
Deployment stage: prod <-- Default
Security:         AWS IAM <-- Default
```
Click the **Next** button.

### Configure function

```
Name:        base
Description: <null>
Runtime:     node.js 6.10
```
**Lambda function code**

```
Code entry type: Upload a .zip file
```

Click the Upload button and choose the zip file created earlier.

Accept all other defaults.

**Lambda function handler and role**

```
Handler:          index.handler
Role:             Create new role from template(s)
Role name:        role
Policy templates: <null>
```
Accept all other defaults.

Click the **Next** button.

### Review

Click the **Create function** button.

Function is created and you are navigated to the Lambda > Functions page for the function.

### Function

Click the Test button.

```
Sample event template: Hello World
```

Click the **Save and test** button.

## Cleaning up

To clean up:

* Delete the function in Lambda.
* Delete the role in IAM.
* Delete the service in API Gateway.
