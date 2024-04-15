import { useState, useEffect, useCallback } from "react";

export default function RandomColor() {
    const [typeOfColor, setTypeOfColor] = useState('hex');
    const [color, setColor] = useState('#000000');

    function randomColorUtility(length) {
        return Math.floor(Math.random() * length);
    }

    const handleCreateRandomHexColor = useCallback(() => {
        const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'];
        let hexColor = "#";

        for (let i = 0; i < 6; i++) {
            hexColor += hex[randomColorUtility(hex.length)];
        }

        setColor(hexColor);
    }, []);

    const handleCreateRandomRgbColor = useCallback(() => {
        const r = randomColorUtility(256);
        const g = randomColorUtility(256);
        const b = randomColorUtility(256);

        setColor(`rgb(${r}, ${g}, ${b})`);
    }, []);

    useEffect(() => {
        if (typeOfColor === 'rgb') handleCreateRandomRgbColor();
        else handleCreateRandomHexColor();
    }, [typeOfColor, handleCreateRandomRgbColor, handleCreateRandomHexColor]);

    return (
        <div style={{
            width : '100vw',
            height : '100vh',
            backgroundColor : color
        }}>
            <button onClick={() => setTypeOfColor('hex')}>Create Hex Color</button>
            <button onClick={() => setTypeOfColor('rgb')}>Create RGB Color</button>
            <button onClick={typeOfColor === 'hex' ? handleCreateRandomHexColor : handleCreateRandomRgbColor}>Generate Random Color</button>

            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                color: '#fff',
                fontSize: '60px',
                marginTop: '25px',
                flexDirection: 'column',
                gap: '10px'
            }}>
                <h3>{typeOfColor === 'rgb' ? 'RGB Color' : 'Hex Color'}</h3>
                <h1>{color}</h1>

            </div>
        </div>
    );
}