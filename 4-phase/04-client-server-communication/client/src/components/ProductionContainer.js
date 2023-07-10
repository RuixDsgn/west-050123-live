import Production from "./Production"

const ProductionContainer = ({ productions }) => {
	const mappedProductions = () =>
		productions.map((prod) => <Production {...prod} />)

	return <div>{mappedProductions()}</div>
}

export default ProductionContainer
