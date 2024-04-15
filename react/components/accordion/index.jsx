import { useState } from "react";
import data from "./data";
import './styles.css'

export default function Accordion() {
    const [selected, setSelected] = useState(null);
    const [enableMultiSelection, setEnableMultiSelection] = useState(false);
    const [multiple, setMultiple] = useState([]);
    const [selectedClass, setSelectedClass] = useState('');

    function resetSelections() {
        setEnableMultiSelection(!enableMultiSelection);
        setSelectedClass(enableMultiSelection ? '' : 'selected');
        setSelected(null);
        setMultiple([]);
    }

    function handleSingleSelection(getCurrentId) {
        setSelected(getCurrentId === selected ? null : getCurrentId);
    }

    function handleMultiSelection(getCurrentId) {
        let cpyMultiple = [...multiple];
        const findIndexOfCurrentId = cpyMultiple.indexOf(getCurrentId);

        if (findIndexOfCurrentId === -1) cpyMultiple.push(getCurrentId);
        else cpyMultiple.splice(findIndexOfCurrentId, 1);

        setMultiple(cpyMultiple);
    }

    return <div className="wrapper">
        <button className={selectedClass} onClick={() => resetSelections()}>Enable Multi Selection</button>
        <div className="accordion">
            {
                data && data.length > 0 ?
                data.map(dataItem =>
                    <div key={dataItem.id} className="item">
                        <div onClick={ enableMultiSelection ? () => handleMultiSelection(dataItem.id) : () => handleSingleSelection(dataItem.id)} className="title">
                            <h3>{dataItem.question}</h3>
                            <span>+</span>
                        </div>
                        {
                            enableMultiSelection ? 
                            multiple.indexOf(dataItem.id) !== -1 &&
                            <div className="content">{dataItem.answer}</div> :
                            selected === dataItem.id && <div className="content">{dataItem.answer}</div>
                        }
                    {/*                         
                        {
                            selected === dataItem.id || multiple.indexOf(dataItem.id) !== -1 ?
                            <div className="content">{dataItem.answer}</div>
                            : null
                        }
                    */}
                    </div>
                )
                : <div>No data found!</div>
            }
        </div>
    </div>;
 }