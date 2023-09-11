import { createSlice } from '@reduxjs/toolkit'

const initialState ={
    productList:[]  //the same
}

const productSlice = createSlice({
    name:"product",
    initialState,
    reducers:{
        addProductList:(state,action)=>{
            state.productList = action.payload //the same state
        }
    }
})

export const {addProductList} = productSlice.actions
export default productSlice.reducer