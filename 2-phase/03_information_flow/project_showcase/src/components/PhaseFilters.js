import React, { useState } from "react"

const PhaseFilters = ({setPhase}) => {
	// const [phase, setPhase] = useState(0)

	const handleClick = (e) => {
		setPhase(Number(e.target.name))
	}
	return (
		<div className="filter">
			<button onClick={handleClick} name={0}>All</button>
			<button onClick={handleClick} name={5}>Phase 5</button>
			<button onClick={handleClick} name={4}>Phase 4</button>
			<button onClick={handleClick} name={3}>Phase 3</button>
			<button onClick={handleClick} name={2}>Phase 2</button>
			<button onClick={handleClick} name={1}>Phase 1</button>
		</div>
	)
}

export default PhaseFilters


/* Creating a filter button for the different phases	
 - Set a state variable and a setter function
 - Create an onClick event, that when clicked, will call on the handleClick function
	- handleClick function, when called will set the phase to the phase number that was clicked
 - Lift the state to the Project container because this component holds the data that will be rendered when filtered
 - Set the value of <PhaseFilter /> in ProjectContainer with setPhase={setPhase} to pass it down as prop in PhaseFilters
 - in ProjectContainer:
    - Prioritze filtering before sorting, this way, when a user sorts, less content will pop up bc its been filtered
	- Create a conditional statement that will render the filtered results depending on the phase (line 18)
	- In line 22, change the projects.filter to phaseResults.filter so it will sort the filtered projects when using the search bar
	- in line 32, change to value of projects into searchResults 
*/