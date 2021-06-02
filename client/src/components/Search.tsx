import { ChangeEvent, useState } from 'react';

function Search() {
	const [searchValue, setSearchValue] = useState('');

	const changeHandler = (e: ChangeEvent<HTMLInputElement>) => {
		setSearchValue(e.target.value);
	};
	const submitHandler = async () => {
		const res = await fetch(
			`http://localhost:8000/listings/?search=${searchValue}`
		);
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
