import { useState } from "react"
import PhaseFilters from "./PhaseFilters"
import SearchInput from "./SearchInput"
import ProjectList from "./ProjectList"

const ProjectContainer = () => {
	const [projects, setProjects] = useState([])
	const [searchQuery, setSearchQuery] = useState("")
	const [phase, setPhase] = useState(0)
	

	const handleClick = () => {
		fetch("http://localhost:3000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const phaseResults = !!phase ? projects.filter(project => {
		return project.phase === phase
	}) : projects

	const searchResults = phaseResults.filter((project) => {
		return project.name.toLowerCase().includes(searchQuery.toLowerCase())
	})

	return (
		<section>
			<button onClick={handleClick}>Load Projects</button>
			<h2>Projects</h2>
			<PhaseFilters setPhase={setPhase} />
			<SearchInput setSearchQuery={setSearchQuery} />
			<ProjectList projects={searchResults} />
		</section>
	)
}

export default ProjectContainer
