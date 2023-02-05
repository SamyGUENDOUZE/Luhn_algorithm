// 4624748233249080

// Fonction qui me permet de vérifier si l'input est valide ou pas
function validateNumbers(numbers) {
    // numbers.replace(/ /g, "")
    // console.log(numbers)
    let numberReg = /^[0-9]{16}$/
    return numberReg.test(numbers)
}

function getValue() {
    card_number = (document.getElementById("number")).value;

    if (validateNumbers(card_number) == false){
        alert('formulaire invalide')
    }
    else{
        let card_number_list = String(card_number).split("").map((card_number)=>{
            return Number(card_number)
          })
        
        
        inverted_list = card_number_list.reverse()
    
        liste_index_pair = []
        liste_index_impair = []
    
        for (let i = 0; i < 16; i++) {
            if (i % 2 == 0) {
                liste_index_pair.push(inverted_list[i])
            }
            else {
                liste_index_impair.push(inverted_list[i])
            }
        }
    
        let sum_pair = 0
        let sum_impair = 0
    
        for(var impair of liste_index_impair){
            impair = 2 * impair
            if (impair > 9) {
                impair = String(impair).split("").map((impair) => {
                return Number(impair)
              })
            impair = impair[0] + impair[1] 
            }
            sum_impair += impair
        }
    
        for(var pair of liste_index_pair){
            sum_pair += pair
            
        }
    
        let final_number = sum_impair + sum_pair
        if (final_number % 10 == 0) { 
            alert('La carte est valide selon l\'algorithme de Luhn')
        }
        else {
            alert('La carte n\'est pas valide selon l\'algorithme de Luhn')
        }
    }
    }