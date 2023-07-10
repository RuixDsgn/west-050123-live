import { useState, useEffect } from "react"
import { Routes, Route, useNavigate } from "react-router"
import Home from "./components/Home"
import Nav from "./components/Nav"
import ProductionContainer from "./components/ProductionContainer"
import ProductionDetail from "./components/ProductionDetail"
import ProductionForm from "./components/ProductionForm"

// Routes => Switch

const App = () => {
	const [productions, setProductions] = useState([])
	const nav = useNavigate()
	useEffect(() => {
		fetchAllProductions()
	}, [])

	const fetchAllProductions = () => {
		fetch("http://127.0.0.1:5555/productions")
			.then((res) => res.json())
			.then((allProductions) => {
				console.log(allProductions)
				setProductions(allProductions)
			})
	}

	const postProduction = (productionFormData) => {
		const postReqObj = {
			method: "POST",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(productionFormData),
		}
		fetch("http://127.0.0.1:5555/productions", postReqObj)
			.then((res) => res.json())
			.then((newProductionObj) => {
				console.log(newProductionObj)
				// If it works:  add to our productions state
				setProductions([...productions, newProductionObj])
				nav(`/productions/${newProductionObj.id}`)
			})
	}

	return (
		<div>
			<Nav />
			<Routes>
				<Route
					exact
					path="/productions/new"
					element={<ProductionForm postProduction={postProduction} />}
				/>
				<Route path="/productions/:id" element={<ProductionDetail />} />
				<Route
					path="/productions"
					element={<ProductionContainer productions={productions} />}
				/>
				<Route path="/" element={<Home />} />
			</Routes>
		</div>
	)
}

export default App
