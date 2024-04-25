function updateTheJson() {
    // const fs = require('fs');
    const fs = require('fs');

    // Read JSON file
    const userData = JSON.parse(fs.readFileSync('C:\\xampp\\htdocs\\Crazyhomes\\jsonfiles\\data.json', 'utf8'));

    // Define array declaration in JavaScript
    const jsArrayDeclaration = 'const usersData = ' + (userData) + ';';

    // Write array declaration to JavaScript file
    fs.writeFileSync('users_array.js', jsArrayDeclaration);

    console.log("Data has been stored in users_array.js");
}

// module.exports = {
//     updateTheJson: updateTheJson
// };