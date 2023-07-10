import { useState, useEffect } from "react"
import { Routes, Route, useNavigate } from "react-router"
import Home from "./components/Home"
import Nav from "./components/Nav"
import ProductionContainer from "./components/ProductionContainer"
import ProductionDetail from "./components/ProductionDetail"
import ProductionForm from "./components/ProductionForm"
import NotFound from "./components/NotFound"
import ProductionEditForm from "./components/ProductionEditForm"

const App = () => {
	const [productions, setProductions] = useState([])
	// This will either be null OR the production we are going to edit
	const [editProduction, setEditProduction] = useState(null)
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

	const patchProduction = (productionFormData, id) => {
		const patchReqObj = {
			method: "PATCH",
			headers: {
				"Content-type": "application/json",
			},
			body: JSON.stringify(productionFormData),
		}
		fetch(`http://127.0.0.1:5555/productions/${id}`, patchReqObj)
			.then((res) => res.json())
			.then((updatedProduction) => {
				console.log(updatedProduction)
				// if successful, update our state to reflect the change
				setProductions((prevProds) =>
					prevProds.map((p) => (p.id === id ? updatedProduction : p))
				)
				nav(`/productions`)
				// nav(`/productions/${id}`)
			})
	}

	const deleteProduction = (id) => {
		fetch(`http://127.0.0.1:5555/productions/${id}`, { method: "DELETE" })
		.then(data => {
			console.log(data)
			setProductions(prevProds => prevProds.filter(p => p.id !== id))
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
				<Route
					path="/productions/edit/:id"
					element={
						<ProductionEditForm
							editProduction={editProduction}
							patchProduction={patchProduction}
						/>
					}
				/>
				<Route path="/productions/:id" element={<ProductionDetail />} />
				<Route
					path="/productions"
					element={
						<ProductionContainer
							productions={productions}
							setEditProduction={setEditProduction}
							deleteProduction={deleteProduction}
						/>
					}
				/>
				<Route path="/" element={<Home />} />
				<Route path="*" element={<NotFound />} />
			</Routes>
		</div>
	)
}

export default App
