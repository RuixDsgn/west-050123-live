import Production from "./Production"

const ProductionContainer = ({
	productions,
	setEditProduction,
	deleteProduction,
}) => {
	const mappedProductions = () =>
		productions.map((prod) => (
			<Production
				key={prod.id}
				production={prod}
				setEditProduction={setEditProduction}
				deleteProduction={deleteProduction}
			/>
		))

	return <div>{mappedProductions()}</div>
}

export default ProductionContainer
