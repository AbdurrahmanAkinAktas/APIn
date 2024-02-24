// Simple check for the response code. Just to make sure the endpoint exists and return something
client.test("Request executed successfully", function() {
        client.assert(response.status === 200, "Response status is not 200");
});