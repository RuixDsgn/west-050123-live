import { useState, useEffect } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"
import ProjectEditForm from "./components/ProjectEditForm"

/* 

	Component LifeCycle????

	1. Mount
		useEffect(cbFunc, [])
	2. Updating
		useEffect(cbFunc)
			- NEVER PUT `STATE CHANGE or worse A FETCH` INSIDE A NO DEP ARRAY
		useEffect(cbFunc, [someStateThingHere])
	3. Unmounting
		- useEffect(() => {
			functions
			Other functions
			return () => {
				cleanup our app function
			}
		}, [states])

*/

const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	useEffect(() => {
		console.log("EVERYCHANGE OF STATE ON APP")
	})
	// * COMPONENT DID MOUNT
	useEffect(() => {
		console.log("LOAD PROJECTS")
		fetchAllProjects()

		return () => {
			console.log("cleanup")
			setProjects([])
		}
	}, [])

	const fetchAllProjects = () => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const onUpdateProjects = (updatedProject) => {
		// update ONLY the project of id with this new project obj
		// setProject(with a map and only change the project of id)
		// const mappedEditProjects = projects.map(proj => {
		// 	if (proj.id === updatedProject.id) {
		// 		return updatedProject
		// 	} else {
		// 		return proj
		// 	}
		// })
		setProjects((prevProj) =>
			prevProj.map((proj) =>
				proj.id === updatedProject.id ? updatedProject : proj
			)
		)
	}

	const onDeleteProject = (id) => {
		setProjects((prevProj) => prevProj.filter((proj) => id !== proj.id))
	}

	const dark = isDarkMode ? "App" : "App light"

	return (
		<div className={dark}>
			<Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
			{/* <ProjectForm setProjects={setProjects} /> */}
			{/* <ProjectEditForm
				editProject={projects[0]}
				onUpdateProjects={onUpdateProjects}
			/> */}
			<ProjectContainer
				projects={projects}
				onUpdateProjects={onUpdateProjects}
				onDeleteProject={onDeleteProject}
			/>
		</div>
	)
}

export default App
