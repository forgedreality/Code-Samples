import { useEffect, useState } from "react";
import './styles.css';

export default function LoadMoreData({url, limit=20}) {
    const [loading, setLoading] = useState(false);
    const [products, setProducts] = useState([]);
    const [count, setCount] = useState(0);
    const [disableButton, setDisableButton] = useState(false);

    async function fetchProducts() {
        try {
            setLoading(true);
            const response = await fetch(`${url}?limit=${limit}&skip=${count === 0 ? 0 : count * limit}`);
            const result = await response.json();

            if (result && result.products && result.products.length) {
                setProducts((prevData) => [...prevData, ...result.products]);
                setLoading(false);
            }
        } catch(e) {
            console.log(e);
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchProducts();
    }, [count]);

    useEffect(() => {
        if (products && products.length === 100) setDisableButton(true);
    }, [products]);

    if (loading) {
        return <div>Loading data! Please wait.</div>;
    }

    return <div className="load-more-container">
        <div className="product-container">
            {
                products && products.length ?
                    products.map(item => ( <div className="product" key={item.id}>
                        <img src={item.thumbnail} alt={item.title} />
                        <p>{item.title}</p>
                    </div>)) : null
            }
        </div>
        <div className="button-container">
            <button disabled={disableButton} onClick={() => setCount(count + 1)}>Load More Products</button>
            {
                disableButton ? <p>
                    You have reached 100 products.
                </p> : null
            }
        </div>
    </div>
}