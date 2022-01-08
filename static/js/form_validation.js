// functions to add or remove classes and show and hyde validation errrors copied
// from my project portfolio 2 Change Fuel
// https://github.com/JoGorska/Keto-diet/blob/master/assets/js/calculator.js
/**
 * Function to add class
 * @param {*} className 
 * @param {*} targetNode 
 */
 function addClass(className, targetNode) {
    targetNode.classList.add(className);
  }
  
  /**
   * Function to remove class
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function removeClass(className, targetNode){
    targetNode.classList.remove(className);
  }
  
  /**
   * Function to set attribute
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function setAtribute(atributeName, atributeValue, targetNode) {
    targetNode.setAttribute(atributeName, atributeValue);
  }
  /**
   * Function to remove attribute
   * @param {*} atributeName 
   * @param {*} atributeValue 
   * @param {*} targetNode 
   */
  function removeAtribute(atributeName, atributeValue, targetNode) {
    targetNode.removeAttribute(atributeName, atributeValue);
  }
  
  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
  function displayErrorValidation(targetNodeInput, targetNodeHelp) {
  
    addClass("is-invalid",targetNodeInput);
    setAtribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("invalid-feedback", targetNodeHelp);
  
  }

  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */

   function displayPassedValidation(targetNodeInput, targetNodeHelp) {
  
    addClass("is-valid",targetNodeInput);
    setAtribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("valid-feedback", targetNodeHelp);
  
  }
  
  /**
   * Function to remove display Error after validation has been passed
   * makes div with help message invisible, input border comes back to standard and icon with exclamation mark disapears
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
  function removeErrorValidation(targetNodeInput, targetNodeHelp) {
  
    removeClass("is-invalid",targetNodeInput);
    removeAtribute("aria-describedby", "name-help", targetNodeInput);
    addClass("my-invisible", targetNodeHelp);
    removeClass("invalid-feedback", targetNodeHelp);
  }
  

function validateGeolocationFound() {
    // need to check if all long and lat has been loaded
    // but display feedback in help node for address
    // because I don't want to show coordinates to the user, too much
    // information
    
}