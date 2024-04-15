# Print Prime Numbers
# https://www.hackerrank.com/challenges/print-prime-numbers/problem
DELIMITER $$
CREATE PROCEDURE print_primes(num INT)
    BEGIN
        DECLARE result LONGTEXT;
        DECLARE prime INT;
        DECLARE divisor INT;
        DECLARE isPrime BIT;
        SET prime = 1;
        SET result = "2";
        WHILE prime <= num DO
            SET prime = prime + 2;
            SET divisor = 2;
            SET isPrime = 1;
            WHILE divisor <= FLOOR(SQRT(prime)) DO
                IF prime % divisor = 0 THEN
                    SET isPrime = 0;
                END IF;
                SET divisor = divisor + 1;
            END WHILE;
            IF isPrime = 1 THEN
                SET result = CONCAT(result, "&", prime);
            END IF;
        END WHILE;
        SELECT result;
    END
$$

CALL print_primes(1000);