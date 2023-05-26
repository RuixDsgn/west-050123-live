import { useState } from "react"
import Header from "./components/Header"
import ProjectForm from "./components/ProjectForm"
import ProjectList from "./components/ProjectList"

import projects from "./projects"

const App = () => {

const [isDarkMode, setIsDarkMode] = useState(true)

	return (
		<div className={`App${isDarkMode ? "" : " light" }`}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			<ProjectForm />
			<ProjectList projects={projects} />
		</div>
	)
}

export default App
