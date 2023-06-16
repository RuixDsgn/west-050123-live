const PhaseFilters = ({ setPhase }) => {

	const handleClick = (e) => {
		setPhase(Number(e.target.name))
	}
	return (
		<div className="filter">
			<button onClick={handleClick} name={0}>
				All
			</button>
			<button onClick={() => setPhase(5)}>Phase 5</button>
			<button onClick={() => setPhase(4)}>Phase 4</button>
			<button onClick={() => setPhase(3)}>Phase 3</button>
			<button onClick={() => setPhase(2)}>Phase 2</button>
			<button onClick={() => setPhase(1)}>Phase 1</button>
		</div>
	)
}

export default PhaseFilters
