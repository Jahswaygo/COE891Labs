/**
 * This Source Code Form is subject to the terms of the Mozilla Public License,
 * v. 2.0. If a copy of the MPL was not distributed with this file, You can
 * obtain one at http://mozilla.org/MPL/2.0/. OpenMRS is also distributed under
 * the terms of the Healthcare Disclaimer located at http://openmrs.org/license.
 *
 * Copyright (C) OpenMRS Inc. OpenMRS is a registered trademark and the OpenMRS
 * graphic logo is a trademark of OpenMRS Inc.
 */
package org.openmrs;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.when;

import java.util.Date;

import org.junit.jupiter.api.Test;
import org.openmrs.order.OrderUtilTest;

/**
 * Contains tests for DrugOrder
 */
public class Jahs_DrugOrderTest {

	// TC1: Happy Path - All fields set correctly
	@Test
	public void testClone_AllFieldsPopulated() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());

		Drug drug = new Drug();
		drug.setConcept(new Concept());
		order.setDrug(drug);

		order.setOrderType(new OrderType());
		order.setDrugNonCoded("Paracetamol");

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals(order.getPatient(), clone.getPatient());
		assertEquals(order.getCareSetting(), clone.getCareSetting());
		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(order.getConcept(), clone.getConcept());
		assertEquals(order.getOrderType(), clone.getOrderType());
		assertEquals(order.getDrugNonCoded(), clone.getDrugNonCoded());
		assertEquals(order, clone.getPreviousOrder());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	// TC2: Null Patient
	@Test
	public void testClone_NullPatient() {
		DrugOrder order = new DrugOrder();
		order.setPatient(null);
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setOrderType(new OrderType());

		DrugOrder clone = order.cloneForDiscontinuing();

		assertNull(clone.getPatient());
		assertEquals(order.getCareSetting(), clone.getCareSetting());
		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(order.getOrderType(), clone.getOrderType());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	// TC3: Null CareSetting
	@Test
	public void testClone_NullCareSetting() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(null);
		order.setDrug(new Drug());
		order.setOrderType(new OrderType());

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals(order.getPatient(), clone.getPatient());
		assertNull(clone.getCareSetting());
		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	// TC4: Null Drug (and thus Concept)
	@Test
	public void testClone_NullDrug() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(null);
		order.setOrderType(new OrderType());

		DrugOrder clone = order.cloneForDiscontinuing();

		assertNull(clone.getDrug());
		assertNull(clone.getConcept());
		assertEquals(order.getOrderType(), clone.getOrderType());
	}

	// TC5: Null OrderType
	@Test
	public void testClone_NullOrderType() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setOrderType(null);

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals(order.getDrug(), clone.getDrug());
		assertNull(clone.getOrderType());
	}

	// TC6: Empty drugNonCoded string
	@Test
	public void testClone_EmptyDrugNonCoded() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setOrderType(new OrderType());
		order.setDrugNonCoded("");

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals("", clone.getDrugNonCoded());
	}

	// Additional Test: Null DrugNonCoded
	@Test
	public void testClone_NullDrugNonCoded() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setOrderType(new OrderType());
		order.setDrugNonCoded(null);

		DrugOrder clone = order.cloneForDiscontinuing();

		assertNull(clone.getDrugNonCoded());
		assertEquals(order.getPatient(), clone.getPatient());
		assertEquals(order.getCareSetting(), clone.getCareSetting());
		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(order.getOrderType(), clone.getOrderType());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	// Additional Test: Mixed Coded and Non-Coded Drugs
	@Test
	public void testClone_MixedCodedAndNonCodedDrugs() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setDrugNonCoded("Paracetamol");
		order.setOrderType(new OrderType());

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(order.getDrugNonCoded(), clone.getDrugNonCoded());
		assertEquals(order.getPatient(), clone.getPatient());
		assertEquals(order.getCareSetting(), clone.getCareSetting());
		assertEquals(order.getOrderType(), clone.getOrderType());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	// Additional Test: Default Optional Fields
	@Test
	public void testClone_DefaultOptionalFields() {
		DrugOrder order = new DrugOrder();
		order.setPatient(new Patient());
		order.setCareSetting(new CareSetting());
		order.setDrug(new Drug());
		order.setOrderType(new OrderType());

		// Leave optional fields at their default values
		order.setAsNeeded(false);
		order.setDose(null);
		order.setFrequency(null);

		DrugOrder clone = order.cloneForDiscontinuing();

		assertEquals(order.getAsNeeded(), clone.getAsNeeded());
		assertNull(clone.getDose());
		assertNull(clone.getFrequency());
		assertEquals(order.getPatient(), clone.getPatient());
		assertEquals(order.getCareSetting(), clone.getCareSetting());
		assertEquals(order.getDrug(), clone.getDrug());
		assertEquals(order.getOrderType(), clone.getOrderType());
		assertEquals(Order.Action.DISCONTINUE, clone.getAction());
	}

	@Test
	public void hasSameOrderableAs_shouldReturnFalseIfSuperHasSameOrderableAsReturnsFalse() {
		DrugOrder order = new DrugOrder();
		Order otherOrder = mock(Order.class);
		when(otherOrder.hasSameOrderableAs(order)).thenReturn(false);

		assertFalse(order.hasSameOrderableAs(otherOrder)); // P1 = true
	}

	@Test
	public void hasSameOrderableAs_shouldReturnFalseIfOtherOrderIsNotADrugOrder() {
		DrugOrder order = new DrugOrder();
		Order otherOrder = new Order();

		assertFalse(order.hasSameOrderableAs(otherOrder)); // P2 = true
	}

	@Test
	public void hasSameOrderableAs_shouldReturnTrueForNonCodedDrugsMatching() {
		DrugOrder order = new DrugOrder();
		order.setDrugNonCoded("Aspirin");

		DrugOrder otherOrder = new DrugOrder();
		otherOrder.setDrugNonCoded("aspirin");

		assertTrue(order.hasSameOrderableAs(otherOrder)); // A = true, B = false
	}

	@Test
	public void hasSameOrderableAs_shouldReturnFalseForNonCodedDrugsNotMatching() {
		DrugOrder order = new DrugOrder();
		order.setDrugNonCoded("Aspirin");

		DrugOrder otherOrder = new DrugOrder();
		otherOrder.setDrugNonCoded("Paracetamol");

		assertFalse(order.hasSameOrderableAs(otherOrder)); // A = true, B = false
	}

	@Test
	public void hasSameOrderableAs_shouldReturnTrueForMatchingCodedDrugs() {
		Drug drug = new Drug();
		drug.setName("Aspirin");

		DrugOrder order = new DrugOrder();
		order.setDrug(drug);

		DrugOrder otherOrder = new DrugOrder();
		otherOrder.setDrug(drug);

		assertTrue(order.hasSameOrderableAs(otherOrder)); // P4 = true
	}

	@Test
	public void hasSameOrderableAs_shouldReturnFalseForNonMatchingCodedDrugs() {
		Drug drug1 = new Drug();
		drug1.setName("Aspirin");

		Drug drug2 = new Drug();
		drug2.setName("Paracetamol");

		DrugOrder order = new DrugOrder();
		order.setDrug(drug1);

		DrugOrder otherOrder = new DrugOrder();
		otherOrder.setDrug(drug2);

		assertFalse(order.hasSameOrderableAs(otherOrder)); // P4 = false
	}
}
