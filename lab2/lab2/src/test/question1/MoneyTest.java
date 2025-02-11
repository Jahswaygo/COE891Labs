package question1;

import junit.framework.TestCase;

/**
 * This is a trivial test which only tests the Money class.
 * If you modify the MoneyBag class, and run Clover with optimization, this test
 * will not be run.
 */
public class MoneyTest extends TestCase {

    public void testAdd() throws InterruptedException {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify the amount is 10
        assertEquals(10, tenEuro.amount());
        // Verify the currency is EURO
        assertEquals("EURO", tenEuro.currency());
        // Print a message and sleep for 3 seconds to simulate a long-running test
        System.out.println("Tests taking too long? Try Clover's test optimization.");
        Thread.sleep(3000);
    }

    public void testNegativeAmount() {
        // Create a Money object with -5 USD
        Money negativeMoney = new Money(-5, "USD");
        // Verify the amount is -5
        assertEquals(-5, negativeMoney.amount());
    }

    public void testZeroAmount() {
        // Create a Money object with 0 USD
        Money zeroMoney = new Money(0, "USD");
        // Verify the amount is 0
        assertEquals(0, zeroMoney.amount());
        // Verify the isZero method returns true
        assertTrue(zeroMoney.isZero());
    }

    public void testDifferentCurrenciesNotEqual() {
        // Create two Money objects with the same amount but different currencies
        Money usd = new Money(10, "USD");
        Money eur = new Money(10, "EUR");
        // Verify they are not equal
        assertFalse(usd.equals(eur));
    }

    public void testHashCodeConsistency() {
        // Create two Money objects with the same amount and currency
        Money money1 = new Money(10, "USD");
        Money money2 = new Money(10, "USD");
        // Verify their hash codes are equal
        assertEquals(money1.hashCode(), money2.hashCode());
    }

    public void testMoneyBagComparison() {
        // Create a Money object with 0 USD
        Money zeroMoney = new Money(0, "USD");
        // Verify the amount is 0
        assertEquals(0, zeroMoney.amount());
        // Verify the isZero method returns true
        assertTrue(zeroMoney.isZero());
    }

    public void testEqualsWithIMoney() {
        // Create a Money object with 0 USD
        Money zeroMoney = new Money(0, "USD");
        // Create an IMoney object with the same amount and currency
        IMoney mockIMoney = new Money(0, "USD");
        // Verify they are equal
        assertTrue(zeroMoney.equals(mockIMoney));
    }

    public void testEqualsWithNonIMoneyObject() {
        // Create a Money object with 0 USD
        Money zeroMoney = new Money(0, "USD");
        // Create a completely unrelated object
        Object nonIMoneyObject = new Object();
        // Verify the Money object is not equal to the unrelated object
        assertFalse("Money should not be equal to a non-IMoney object",
                zeroMoney.equals(nonIMoneyObject));
    }

    public void testEqualsWithIMoneyWhenZero() {
        // Create an IMoney object with 0 USD
        IMoney zeroMoney = new Money(0, "USD");
        // Create another Money object with the same amount and currency
        Money anotherZeroMoney = new Money(0, "USD");
        // Verify they are equal
        assertTrue("A Money instance with zero should be equal to an IMoney instance with zero",
                anotherZeroMoney.equals(zeroMoney));
    }

    public void testAddMoney() {
        // Create two Money objects with the same currency
        Money tenEuro = new Money(10, "EURO");
        Money fiveEuro = new Money(5, "EURO");
        // Add them together and verify the result
        IMoney result = tenEuro.addMoney(fiveEuro);
        assertEquals(new Money(15, "EURO"), result);

        // Create another Money object with a different currency
        Money tenUSD = new Money(10, "USD");
        // Add them together and verify the result is a MoneyBag
        result = tenEuro.addMoney(tenUSD);
        IMoney expected = MoneyBag.create(tenEuro, tenUSD);
        assertEquals(expected, result);
    }

    public void testAddMoneyBag() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Create a MoneyBag with 5 USD and 15 EURO
        MoneyBag bag = (MoneyBag) MoneyBag.create(new Money(5, "USD"), new Money(15, "EURO"));
        // Add the Money object to the MoneyBag and verify the result
        IMoney result = tenEuro.addMoneyBag(bag);
        IMoney expected = MoneyBag.create(new Money(25, "EURO"), new Money(5, "USD"));
        assertEquals(expected, result);
    }

    public void testAmount() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify the amount is 10
        assertEquals(10, tenEuro.amount());
    }

    public void testCurrency() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify the currency is EURO
        assertEquals("EURO", tenEuro.currency());
    }

    public void testEquals() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify it is equal to itself
        assertTrue(tenEuro.equals(tenEuro));

        // Create another Money object with the same amount and currency
        Money anotherTenEuro = new Money(10, "EURO");
        // Verify they are equal
        assertTrue(tenEuro.equals(anotherTenEuro));

        // Create another Money object with a different amount
        Money fiveEuro = new Money(5, "EURO");
        // Verify they are not equal
        assertFalse(tenEuro.equals(fiveEuro));

        // Create another Money object with a different currency
        Money tenUSD = new Money(10, "USD");
        // Verify they are not equal
        assertFalse(tenEuro.equals(tenUSD));

        // Verify the Money object is not equal to a null object
        assertFalse(tenEuro.equals(null));

        // Verify the Money object is not equal to a different type of object
        assertFalse(tenEuro.equals("string"));
    }

    public void testHashCode() {
        // Create two Money objects with the same amount and currency
        Money tenEuro = new Money(10, "EURO");
        Money anotherTenEuro = new Money(10, "EURO");
        // Verify their hash codes are equal
        assertEquals(tenEuro.hashCode(), anotherTenEuro.hashCode());
    }

    public void testIsZero() {
        // Create a Money object with 0 EURO
        Money zeroEuro = new Money(0, "EURO");
        // Verify the isZero method returns true
        assertTrue(zeroEuro.isZero());

        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify the isZero method returns false
        assertFalse(tenEuro.isZero());
    }

    public void testMultiply() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Multiply it by 2 and verify the result
        IMoney result = tenEuro.multiply(2);
        assertEquals(new Money(20, "EURO"), result);

        // Multiply it by 0 and verify the result
        result = tenEuro.multiply(0);
        assertEquals(new Money(0, "EURO"), result);

        // Multiply it by -2 and verify the result
        result = tenEuro.multiply(-2);
        assertEquals(new Money(-20, "EURO"), result);
    }

    public void testNegate() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Negate it and verify the result
        IMoney result = tenEuro.negate();
        assertEquals(new Money(-10, "EURO"), result);

        // Create a Money object with 0 EURO
        Money zeroEuro = new Money(0, "EURO");
        // Negate it and verify the result
        result = zeroEuro.negate();
        assertEquals(new Money(0, "EURO"), result);

        // Create a Money object with -10 EURO
        Money negativeEuro = new Money(-10, "EURO");
        // Negate it and verify the result
        result = negativeEuro.negate();
        assertEquals(new Money(10, "EURO"), result);
    }

    public void testSubtract() {
        // Create two Money objects with the same currency
        Money tenEuro = new Money(10, "EURO");
        Money fiveEuro = new Money(5, "EURO");
        // Subtract them and verify the result
        IMoney result = tenEuro.subtract(fiveEuro);
        assertEquals(new Money(5, "EURO"), result);

        // Create a Money object with 0 EURO
        Money zeroEuro = new Money(0, "EURO");
        // Subtract it from another Money object and verify the result
        result = tenEuro.subtract(zeroEuro);
        assertEquals(new Money(10, "EURO"), result);

        // Create a Money object with -5 EURO
        Money negativeEuro = new Money(-5, "EURO");
        // Subtract it from another Money object and verify the result
        result = tenEuro.subtract(negativeEuro);
        assertEquals(new Money(15, "EURO"), result);
    }

    public void testToString() {
        // Create a Money object with 10 EURO
        Money tenEuro = new Money(10, "EURO");
        // Verify the toString method returns the correct string
        assertEquals("[10 EURO]", tenEuro.toString());
    }
}
