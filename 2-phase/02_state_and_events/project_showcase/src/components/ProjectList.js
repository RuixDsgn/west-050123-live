import { useState } from "react"
import ProjectListItem from "./ProjectListItem"

const ProjectList = ({ projects }) => {

const [searchTerm, setSearchTerm] = useState("")

	const projectListItems = projects.filter(proj => {
		return proj.name.toLowerCase().includes(searchTerm)
	}).map((project) => <ProjectListItem key={project.id} project={project} />)

	const handleSearch = (e) => {
		setSearchTerm(e.target.value)
	}

	return (
		<section>
			<h2>Projects</h2>

			<div className="filter">
				<button>All</button>
				<button>Phase 5</button>
				<button>Phase 4</button>
				<button>Phase 3</button>
				<button>Phase 2</button>
				<button>Phase 1</button>
			</div>
			<input type="text" placeholder="Search..." onChange={handleSearch}/>

			<ul className="cards">{projectListItems}</ul>
		</section>
	)
}

export default ProjectList


/* Filtering projects with the search bar using state hook
  - set state variable and setter function and set the state variable to an empty string (line 6)	
  - create an onChange event on the search bar (line 28) and set the event with a function called handleSearch (line 12)
  - use the handleSearch function to set the setter function's value as e.target.value to capture the value being inputted in the search bar(that's why the inital state is set to an empty string)
  - Array Methods
    - to iterate through the array while using the search bar, we want to use the filter then map methods (line 8)
	- when targeting the name of the project, use the lowerCase function to convert the project name into lowercase which will match whatever value is entered in the empty string.
	- if the project name is matched by using the function .includes(), return the project (line 9)
*/