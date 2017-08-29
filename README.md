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
console.log("{\"package\":\"" + package.name + ",\"version\":\"" + package.version +"\"}");
exports.handler = function (event, context) {
  console.log("{\"from\":\"index.exports.handler\",\"to\":\"base.handleRequest\"}");
  base.handleRequest(event, context.done);
}
```

lib/base.js

```javascript
exports.handleRequest = function (requestData, callback) {
  console.log("{\"enter\":\"base.handleRequest\"}");
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

* Navigate to https://console.aws.amazon.com/lambda/home.
* Click the **Create a function** button.

### Step 1 Select blueprint

* Click the **Author from scratch** button.

### Step 2 Configure triggers

* Select the **API Gateway** trigger by clicking the gray, dashed-lined box.
* Click the **Enter value** button where applicable.

```
API name:         rest-implementation
Deployment stage: prod <-- Default
Security:         AWS IAM <-- Default
```
* Click the **Next** button.

### Step 3 Configure function

* Basic information

```
Name:        base
Description: <null>
Runtime:     node.js 6.10
```

* Lambda function code
  * Select **Upload a .ZIP file** from the **Code entry type** drop down menu.
  * Click the **Upload** button for **Function package**.
  * Choose the zip file created earlier.
  * Accept all other defaults.
* Lambda function handler and role

```
Handler:          index.handler
Role:             Create new role from template(s)
Role name:        role
Policy templates: <null>
```

* Accept all other defaults.
* Click the **Next** button at the bottom of the page.

### Step 4 Review

* Click the **Create function** button at the bottom of the page.
* The function is created and you are navigated to the Lambda > Functions page for the function.

### Lambda > Functions > base console.

* Click the **Test** button at the top of the page.
* You should see: "Execution result: succeeded (logs)" with a Details expando.

## Cleaning up

To clean up:

* Delete the function in **Lambda**.
  * Click the **Actions** drop down.
  * Select **Delete function**.
  * Click the **Delete** button to confirm.
* Delete the role in **IAM**.
  * Navigate to https://console.aws.amazon.com/iam/home.
  * Click **Roles** in the sidebar.
  * Place a check next to `role` in the list of roles.
  * Click the **Role actions** drop down.
  * Select **Delete role**.
  * Click the **Yes, Delete** button to confirm.
* Delete the service in **API Gateway**.
  * Navigate to https://us-west-2.console.aws.amazon.com/apigateway/home.
  * Click the hyperlink for `rest-implementation`.
  * Click the **Actions** drop down.
  * Select **Delete API**.
  * Enter the name of the API.
  * Click the **Delete API** button.
