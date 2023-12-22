// Eksempel 1
const userId = req.body.userId;
const query = "SELECT * FROM Users WHERE UserId = '" + userId + "'";

// Eksempel 2
const userId = req.body.userId;
const query = "SELECT * FROM Users WHERE UserId = '" + userId + "' OR 1=1";

// Eksempel 3
const userId = req.body.userId;
const query = "SELECT * FROM Users WHERE UserId = '" + userId + "' UNION SELECT * FROM CreditCards";

// Eksempel 4
const userId = req.body.userId;
const query = "SELECT * FROM Users WHERE UserId = '" + userId.replace(/'/g, "''") + "'";

// Eksempel 5
const userId = req.body.userId;
const query = "SELECT * FROM Users WHERE UserId = '" + mysql_real_escape_string(userId) + "'";


const mysql = require('mysql2');
require('dotenv').config();

const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD
});

// Eksempel 6: Bruke forberedte uttalelser (prepared statements) med brukernavnet "JonasDahl"
const userId = 'JonasDahl';

// Bruk ? som en plassholder for parameteren
const query = "SELECT * FROM Users WHERE UserId = ?";
const values = [userId];

connection.query(query, values, (err, results) => {
  if (err) {
    console.error(err);
    return;
  }

  // Behandle resultatene her
  console.log(results);
});

// Husk å håndtere tilkoblingslukking i virkelige applikasjoner
connection.end();

