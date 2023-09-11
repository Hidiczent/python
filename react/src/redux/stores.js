import { configureStore } from "@reduxjs/toolkit";
import productreducer from "./productreducer";
import cartReducer from "./reducers/cartReducer";

const rootReducer = {
    products: productreducer,
    carts:cartReducer
}

export default configureStore({
    reducer: rootReducer
})