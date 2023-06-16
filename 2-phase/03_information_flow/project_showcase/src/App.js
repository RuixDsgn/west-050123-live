import { useState } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"
import SearchInput from "./components/SearchInput"
import PhaseFilters from "./components/PhaseFilters"

/* 
  1. What's the difference between State and Props?
  - State Dynamic / Props Static*
    - props are immutatable
    - Change in State triggers re-render of the comp tree
  2.  How do we change State?
    // - state = newState?
    setState(newState)  OR setState(prevState => newState)

  3. If our state is going to be an array, what should the datatype of the inital state be?
  - an array
    - Can be `null`, be it more benefical to keep the datatypes consistent

*/

const App = () => {
	// const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)
	// const [searchQuery, setSearchQuery] = useState("")
	
	// const handleClick = () => {
	// 	fetch("http://localhost:3000/projects")
	// 		.then((res) => res.json())
	// 		.then((projects) => setProjects(projects))
	// }

	// const searchResults = projects.filter((project) => {
	// 	return project.name.toLowerCase().includes(searchQuery.toLowerCase())
	// })

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			{/* <ProjectForm />  */}
			<ProjectContainer />
		</div>
	)
}

export default App
