# Data Analysis Assignment

## Challenge 1 — Filter by Category

### Explanation

When the category is changed to `ATLANTIS`, the function returns an empty DataFrame because no records match that department. The selected columns remain visible, but the index is empty because no rows satisfy the filtering condition. This is expected behavior, not an error.

## Challenge 2 — Filter by Numeric Threshold

### Explanation

When the threshold is set to `10`, the filtering operation returns an empty DataFrame because the maximum value in the `cantidad` column is `7`. Consequently, no records satisfy the condition `cantidad > 10`, and the number of matching records is zero.

## Challenge 3 — Filter by Date Range

When the most recent date is provided first, the function returns an empty DataFrame because the start date is later than the end date. No record can satisfy both date conditions simultaneously. The selected columns remain visible, but the index is empty because no rows match the filtering criteria. To obtain the expected results, the start date must be earlier than or equal to the end date.

## Challenge 4 — Filter by Category and Overall Mean

The overall mean of the cantidad column is approximately 1.001682, while the mean for Santander is approximately 1.001487. Although these values are different, both means lie between 1 and 2. Since cantidad contains integer values, both conditions select records with a value of at least 2. Therefore, both approaches return the same 38 records.

In general, the results can differ because a category's mean may be higher or lower than the mean of the entire dataset. This changes the threshold used to filter the records and can therefore change the number of records returned.

## Challenge 5 — Top N Records by Category

When the value of n exceeds the number of records available after filtering the DataFrame, the head(n) method returns all the available records instead of raising an error. This is because head(n) returns up to n records, depending on how many records exist in the DataFrame. Therefore, n represents the maximum number of records to display, not a guaranteed number. If fewer records are available than requested, all existing records are returned.
