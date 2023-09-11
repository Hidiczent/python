import { createSlice } from '@reduxjs/toolkit'
const initialState ={
    cartList :[]  //the same
}
const cartSlice = createSlice({
    name:"cart",
    initialState,
    reducers:{
        addCartItem:(state,action)=>{
            const product =action.payload
            const exist=state.cartList.find((x)=> x.id === product.id)
            if(!exist) state.cartList.push({...product,qty: 1})
        },
        removeCartItem:(state,action)=>{
            // action.payload=index 
            state.cartList.splice(action.payload, 1)
        },
        incrementCartItem:(state,action)=>{
            state.cartList[action.payload].qty +=1
        },
        decrementCartItem:(state,action)=>{
        if (state.cartList[action.payload].qty===1){
            state.cartList.splice(action.payload, 1)
        }
        else {
            state.cartList[action.payload].qty -=1
        }
        }
    }
})
export const {addCartItem,removeCartItem,incrementCartItem,decrementCartItem} = cartSlice.actions
export default cartSlice.reducer