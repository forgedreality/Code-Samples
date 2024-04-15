import './App.css';
// import Accordion from './components/accordion';
// import RandomColor from './components/random-color';
// import StarRating from './components/star-rating';
// import TicTacToe from './components/tic-tac-toe';
// import ImageSlider from './components/image-slider';
// import DataLoader from './components/load-more-data';
// import TreeMenu from './components/tree-menu';
// import menus from './components/tree-menu/data';
// import QrCode from './components/qr-code-generator';
// import QRCodeGenerator from './components/qr-code-generator';
// import LightDarkMode from './components/light-dark-mode';
// import ScrollIndicator from './components/scroll-indicator';
// import TabTest from './components/custom-tabs/tab-test';
import MultiSelect from './components/multiselect';

function App() {
  return (
    <div className="App">
      {/* Tic-Tac-Toe component */}
      {/* <TicTacToe /> */}

      {/* Below are projects from: https://youtu.be/5ZdHfJVAY-s */}

      {/* Accordion component */}
      {/* <Accordion /> */}

      {/* Random color component */}
      {/* <RandomColor /> */}

      {/* Star rating component */}
      {/* <StarRating numOfStars={10} /> */}

      {/* Image slider component */}
      {/* <ImageSlider url={'https://picsum.photos/v2/list'} page={'1'} limit={'10'} /> */}

      {/* Load more products component */}
      {/* <DataLoader url={'https://dummyjson.com/products'} limit={'20'} /> */}

      {/* Tree view menu */}
      {/* <TreeMenu menus={menus} /> */}

      {/* QR code generator */}
      {/* <QRCodeGenerator /> */}

      {/* Light and Dark mode switch */}
      {/* <LightDarkMode /> */}

      {/* Scroll indicator component */}
      {/* <ScrollIndicator url={"https://dummyjson.com/products?limit=100"} /> */}

      {/* Custom tabs component */}
      <TabTest />
    </div>
  );
}

export default App;
