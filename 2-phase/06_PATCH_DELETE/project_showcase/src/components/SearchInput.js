const SearchInput = ({ setSearchQuery }) => {
	const handleOnChange = (e) => setSearchQuery(e.target.value)

	return <input type="text" placeholder="Search..." onChange={handleOnChange} />
}

export default SearchInput
