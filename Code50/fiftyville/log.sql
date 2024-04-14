-- Keep a log of any SQL queries you execute as you solve the mystery.


-- 10:15 AM

-- SELECT * from crime_scene_reports
-- WHERE street = 'Humphrey Street'
-- AND year = 2021
-- AND month = 7
-- AND day = 28;


-- SELECT id from crime_scene_reports
-- WHERE street = 'Humphrey Street'
-- AND year = 2021
-- AND month = 7
-- AND day = 28
-- AND description LIKE '%duck%';

-- SELECT * FROM bakery_security_logs
-- WHERE year = 2021
-- AND month = 7
-- AND day = 28;

-- SELECT * FROM people;

-- SELECT * from phone_calls
-- WHERE year = 2021
-- AND month = 7
-- AND day = 28;


-- SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |

-- | 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |

-- | 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- interviews
-- atm_transactions
-- flights
-- phone_calls
-- bakery_security_logs

-- SELECT * from bakery_security_logs
-- WHERE year = 2021
-- AND month = 7
-- AND day = 28
-- AND hour = 10
-- AND minute BETWEEN 15 AND 25;

-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | id  | year | month | day | hour | minute | activity | license_plate |
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
-- | 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
-- | 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
-- | 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
-- | 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
-- | 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
-- | 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
-- | 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
-- +-----+------+-------+-----+------+--------+----------+---------------+

-- SELECT * from atm_transactions
-- WHERE year = 2021
-- AND month = 7
-- AND day = 28
-- AND transaction_type = 'withdraw'
-- and atm_location = 'Leggett Street';

-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
-- | 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
-- | 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
-- | 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+

-- SELECT * FROM bank_accounts
-- WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);

-- +----------------+-----------+---------------+
-- | account_number | person_id | creation_year |
-- +----------------+-----------+---------------+
-- | 49610011       | 686048    | 2010          |
-- | 26013199       | 514354    | 2012          |
-- | 16153065       | 458378    | 2012          |
-- | 28296815       | 395717    | 2014          |
-- | 25506511       | 396669    | 2014          |
-- | 28500762       | 467400    | 2014          |
-- | 76054385       | 449774    | 2015          |
-- | 81061156       | 438727    | 2018          |
-- +----------------+-----------+---------------+


-- SELECT * FROM people
-- INNER JOIN bank_accounts ON people.id = bank_accounts.person_id
-- WHERE account_number IN (
--     SELECT account_number from atm_transactions
--     WHERE year = 2021
--     AND month = 7
--     AND day = 28
--     AND transaction_type = 'withdraw'
--     and atm_location = 'Leggett Street'
-- )
-- AND license_plate IN (
--     SELECT license_plate from bakery_security_logs
--     WHERE year = 2021
--     AND month = 7
--     AND day = 28
--     AND hour = 10
--     AND minute BETWEEN 15 AND 25
-- );

-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate | account_number | person_id | creation_year |
-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | 49610011       | 686048    | 2010          |
-- | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       | 26013199       | 514354    | 2012          |
-- | 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       | 25506511       | 396669    | 2014          |
-- | 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       | 28500762       | 467400    | 2014          |
-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+


-- SELECT * FROM phone_calls
-- WHERE year = 2021
-- AND month = 7
-- AND day = 28
-- AND duration < 60;

-- +-----+----------------+----------------+------+-------+-----+----------+
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
-- | 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- | 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
-- | 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
-- | 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
-- | 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
-- | 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
-- +-----+----------------+----------------+------+-------+-----+----------+


-- SELECT * FROM people
-- INNER JOIN bank_accounts ON people.id = bank_accounts.person_id
-- WHERE account_number IN (
--     SELECT account_number from atm_transactions
--     WHERE year = 2021
--     AND month = 7
--     AND day = 28
--     AND transaction_type = 'withdraw'
--     and atm_location = 'Leggett Street'
-- )
-- AND license_plate IN (
--     SELECT license_plate from bakery_security_logs
--     WHERE year = 2021
--     AND month = 7
--     AND day = 28
--     AND hour = 10
--     AND minute BETWEEN 15 AND 25
-- )
-- AND phone_number IN (
--     SELECT caller FROM phone_calls
--     WHERE year = 2021
--     AND month = 7
--     AND day = 28
--     AND duration < 60
-- );

-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate | account_number | person_id | creation_year |
-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | 49610011       | 686048    | 2010          |
-- | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       | 26013199       | 514354    | 2012          |
-- +--------+-------+----------------+-----------------+---------------+----------------+-----------+---------------+

-- Thief = Bruce

-- SELECT *
-- FROM people
-- WHERE phone_number = '(375) 555-8161';

-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 864400 | Robin | (375) 555-8161 |                 | 4V16VO0       |
-- +--------+-------+----------------+-----------------+---------------+

-- Accomplice = Robin


-- SELECT * FROM bakery_security_logs
-- WHERE license_plate = '4V16VO0';

-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | id  | year | month | day | hour | minute | activity | license_plate |
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | 248 | 2021 | 7     | 28  | 8    | 50     | entrance | 4V16VO0       |
-- | 249 | 2021 | 7     | 28  | 8    | 50     | exit     | 4V16VO0       |
-- +-----+------+-------+-----+------+--------+----------+---------------+


-- SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers WHERE passport_number = 5773159633);

-- +----+-------------------+------------------------+------+-------+-----+------+--------+
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+


SELECT * FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id IN (SELECT flight_id FROM passengers WHERE passport_number = 5773159633));

-- +----+--------------+-------------------+---------------+
-- | id | abbreviation |     full_name     |     city      |
-- +----+--------------+-------------------+---------------+
-- | 4  | LGA          | LaGuardia Airport | New York City |
-- +----+--------------+-------------------+---------------+

-- Destination: NYC