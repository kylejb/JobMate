import { ChangeEvent, useState } from 'react';

function Search() {
	const [searchValue, setSearchValue] = useState('');

	const changeHandler = (e: ChangeEvent<HTMLInputElement>) => {
		setSearchValue(e.target.value);
	};
	const submitHandler = async () => {
		const url =
			searchValue.length === 0
				? `http://localhost:8000/listings/`
				: `http://localhost:8000/listings/?search=${searchValue}`;
		const res = await fetch(url);
		let data = await res.json();
		console.log(data);
	};
	return (
		<div>
			<input
				type='search'
				value={searchValue}
				placeholder='Search...'
				onChange={changeHandler}
			></input>
			<button type='button' onClick={submitHandler}>
				Search
			</button>
		</div>
	);
}

export default Search;