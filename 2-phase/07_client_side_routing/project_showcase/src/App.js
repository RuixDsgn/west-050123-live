import { useState, useEffect } from "react"

import Header from "./components/Header"
import ProjectContainer from "./components/ProjectContainer"
import ProjectForm from "./components/ProjectForm"
import ProjectEditForm from "./components/ProjectEditForm"
import { Route, Switch } from "react-router-dom/cjs/react-router-dom.min"
import Home from "./components/Home"
import ProjectDetail from "./components/ProjectDetail"

/* 
	WarmUp Questions!

	1. What are the arguments inside the useEffect hook?
		- useEffect(cbFuncion (returns the cleanup funciton), dep array)
	1.a 
		- Component mounting effect hook?
			- Empty Array
	
	2. What is the RETURN of the useState(initialState) hook?
		- console.log(useState(state)) => array of [stateVariable, setterFuction]
		const [state, setState] = useState(initState)

*/

/* 
	Client Side Routing v Server Side Routing

	Server Side
		- Endpoints that serve up info/database/api
		- json-server
		- External/Internal APIs
		- databases, python, flask, django, node/express
		- HIGHLY ENCOURAGED TO BE RESTful Routes!

	Client Side
		- Frontend Routing
		- Can be RESTful Routes, but 
		- URL endpoints with a User Interface
		- in the past, new url in our browser that would point to a NEW HTML file
		- Same process, except without adding new html files
		- Creates a URL Conditional that if the url matches some criteria, then it will display that component tree
		- Gives the ability to go directly to a url on our client side
*/

/* 
	Important React Router Components(v5)

	- <BrowserRouter />
		- A wrapper for the ENTIRE App that gives all the routing functionality to all the child components
	- <Switch />
		- Conditional rendering for the case of the url endpoints
		- Renders the FIRST Route that satifies the url condition
		- if (urlPath.includes("/"))
				<Home />
			else if (urlPath.includes("/this"))
				<ThisComp />
			else if (urlPath === "/that")
				<ThatComp />
		- `exact` will change from approx to exact path name
		
	- <Route />
		- Actual Renders for that endpoint
		- No Props
			=> <Route path="/" component={Component} />
		- With Props
			=> <Route path="/" render={() => <Component props />} />

	- <NavLink />
		- to='path'
	- <Link />

*/

const App = () => {
	const [projects, setProjects] = useState([])
	const [isDarkMode, setIsDarkMode] = useState(true)

	useEffect(() => {
		fetchAllProjects()
	}, [])

	const fetchAllProjects = () => {
		fetch("http://localhost:4000/projects")
			.then((res) => res.json())
			.then((projects) => setProjects(projects))
	}

	const onUpdateProjects = (updatedProject) => {
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
			<Switch>
				<Route
					exact
					path="/projects"
					render={() => (
						<ProjectContainer
							projects={projects}
							onUpdateProjects={onUpdateProjects}
							onDeleteProject={onDeleteProject}
						/>
					)}
				/>
				<Route
					exact
					path="/projects/new"
					render={() => <ProjectForm setProjects={setProjects} />}
				/>
				{/* Dynmaic Route of :id */}
				{/* <Route path="/projects/:id/:name"*/}
				<Route path="/projects/:id" render={() => <ProjectDetail />} />
				<Route path="/projects/:id/edit" render={() => <ProjectEditForm />} />

				<Route path="/" exact component={Home} />
			</Switch>
		</div>
	)
}

export default App
