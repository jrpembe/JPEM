-- DEATHS

select *
from JPEM_PortfolioProject..covidDeaths
where continent is not null
order by 3,4

--select *
--from JPEM_PortfolioProject..covidDeaths
--where continent is not null
--order by 3,4

select location, date, total_cases, new_cases, total_deaths, population
from JPEM_PortfolioProject..covidDeaths
where continent is not null
order by 1,2

-- DeathRate - Likelihood of dying if you contract COVID in your country
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathRate
from JPEM_PortfolioProject..covidDeaths
where location like '%Canada%'
order by 1,2

-- Total cases vs population
select location, date, population, total_cases, (total_cases/population)*100 as PercentInfected
from JPEM_PortfolioProject..covidDeaths
where location like '%Canada%'
order by 1,2

-- Countries with highest infection rate compared to population
select location, population, MAX(total_cases) as Highest_InfectionCount, MAX((total_cases/population))*100 as PercentInfected
from JPEM_PortfolioProject..covidDeaths
--where date between '2020-01-01' and '2021-4-10'
where continent is not null
group by population, location
order by 4 DESC

-- Showing the countries with the highest death count per population
-- if total_deaths had been imported as nvarchar we could cast it as int with the following:
-- select location, MAX((cast(total_deaths as int)/population))*100 as PercentDied
select location, population, MAX(total_deaths) as TotalDeathCount, MAX((total_deaths/population))*100 as PercentDied
from JPEM_PortfolioProject..covidDeaths
--where date between '2020-01-01' and '2021-4-10'
where continent is not null
group by location, population
order by PercentDied DESC

-- Breakdown by location then continent
select location, MAX(total_deaths) as TotalDeathCount
from JPEM_PortfolioProject..covidDeaths
where continent is null and location not like '%income%'
group by location
order by TotalDeathCount DESC

select continent, MAX(total_deaths) as TotalDeathCount
from JPEM_PortfolioProject..covidDeaths
where continent is not null and total_cases is not null and total_deaths is not null
group by continent
order by TotalDeathCount DESC


-- Looking at Global numbers

select sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths)/sum(new_cases))*100 as DeathPercentage
from JPEM_PortfolioProject..covidDeaths
where continent is not null
order by 1,2

-- VACCINATIONS
select death.continent, death.location, death.date, death.population, vaxx.new_vaccinations,
	sum(vaxx.new_vaccinations) OVER (Partition by death.location order by death.location, death.date) as Total_Vaccinations,
	(Total_Vaccinations/death.population)*100 as Percent_Vaccinated
from JPEM_PortfolioProject..covidDeaths as death
join JPEM_PortfolioProject..covidVaccinations as vaxx
	on death.date = vaxx.date and death.location = vaxx.location
where death.continent is not null and death.location like '%Canada%'
order by 2,3

-- Using CTE
-- With Popvs Vac (Continent, Location, Date, Population, Total_Vaccinations)
-- as (   
-- )

-- Temp Table
DROP table if exists #PercentPeopleVaccinated
create table #PercentPeopleVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric,
)

insert into #PercentPeopleVaccinated
select death.continent, death.location, death.date, death.population, vaxx.new_vaccinations,
	sum(vaxx.new_vaccinations) OVER (Partition by death.location order by death.location, death.date) as RollingPeopleVaccinated
from JPEM_PortfolioProject..covidDeaths as death
join JPEM_PortfolioProject..covidVaccinations as vaxx
	on death.date = vaxx.date and death.location = vaxx.location
where death.continent is not null 


select *, (RollingPeopleVaccinated/Population)*100
from #PercentPeopleVaccinated
order by 2,3

-- Creating View to store data for visualization


DROP view if exists PopVaccinated

USE JPEM_PortfolioProject;
GO

CREATE VIEW PercentPopVaccinated AS
SELECT 
    death.continent, 
    death.location, 
    death.date, 
    death.population, 
    vaxx.new_vaccinations,
    SUM(vaxx.new_vaccinations) OVER (
        PARTITION BY death.location 
        ORDER BY death.location, death.date
    ) AS RollingPeopleVaccinated
FROM 
    covidDeaths AS death
JOIN 
    covidVaccinations AS vaxx
        ON death.date = vaxx.date 
        AND death.location = vaxx.location
WHERE 
    death.continent IS NOT NULL;