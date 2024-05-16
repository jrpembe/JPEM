-- Cleaning Dat using SQL Queries

SELECT *
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]




-- Changing Date Format
-- Convert datetime format to Date

SELECT SaleDate, CONVERT(date, SaleDate) as Date
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD SaleDateConverted Date;

UPDATE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
SET SaleDateConverted = CONVERT(date, SaleDate)


-- Populate Property Address Data

SELECT *
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]
--WHERE PropertyAddress is null
ORDER BY ParcelID

-- Using a self join to populate Null values in PropertyAddress

SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing] a
JOIN JPEM_PortfolioProject.[dbo].[NashvilleHousing] b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ]<> b.[UniqueID ]
WHERE a.PropertyAddress is null

UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing] a
JOIN JPEM_PortfolioProject.[dbo].[NashvilleHousing] b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ]<> b.[UniqueID ]
WHERE a.PropertyAddress is null

-- Breaking out Address into Individual Columns (Address, City, State)

-- Property Address

SELECT PropertyAddress
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]
--WHERE PropertyAddress is null
--ORDER BY ParcelID

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) as City
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD PropertySplitAddress Nvarchar(255);

UPDATE NashvilleHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD PropertySplitCity Nvarchar(255);

UPDATE NashvilleHousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))


SELECT *
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]

-- Owner Address
-- Instead of SUBSTRING, this time we will use PARSENAME

SELECT OwnerAddress
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]


SELECT
PARSENAME(REPLACE(OwnerAddress, ',', '.'),3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'),2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]


ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD OwnerSplitAddress Nvarchar(255);

UPDATE NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'),3)

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD OwnerSplitCity Nvarchar(255);

UPDATE NashvilleHousing
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'),2)

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
ADD OwnerSplitState Nvarchar(255);

UPDATE NashvilleHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)

SELECT *
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]


-- Change Y and N to Yes and No in "Sold as Vacant" field

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]
GROUP BY SoldAsVacant
ORDER BY 2

SELECT SoldAsVacant,
	CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
		 WHEN SoldAsVacant = 'N' THEN 'No'
		 ELSE SoldAsVacant
		 END
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]

UPDATE NashvilleHousing
SET SoldAsVacant = 	
		CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
			 WHEN SoldAsVacant = 'N' THEN 'No'
			 ELSE SoldAsVacant
			 END


-- Remove Duplicates (Using RANK or ROWNUMBER)

WITH RowNumCTE as (
SELECT *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				PropertyAddress,
				SalePrice,
				SaleDate,
				LegalReference
	ORDER BY UniqueID
	) Row_Number
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]
--ORDER BY ParcelID
)

SELECT *
FROM RowNumCTE
WHERE Row_Number > 1
ORDER BY PropertyAddress

--DELETE
--FROM RowNumCTE
--WHERE Row_Number > 1



-- Delete Unused Columns

SELECT *
FROM JPEM_PortfolioProject.[dbo].[NashvilleHousing]

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate

ALTER TABLE JPEM_PortfolioProject.[dbo].[NashvilleHousing]
DROP COLUMN SaleDate