# 4624748233249080

while ($true) {s

    $card_number = Read-Host "Entrer un nombre à 16 chiffres et sans espaces"

    if ($card_number-cmatch "[0-9]{16}") {


        # Je convertis le nb en liste et j'inverse cette liste, ?a sera partique pour la suite du code...
        $inverted_list = $card_number -split ""
        [array]::Reverse($inverted_list)
        $inverted_list -join ''

        $liste_index_pair = @() #C'est comme ?a qu'on cr?e un tableau vide en powershell
        $liste_index_impair = @()


        for ($i = 1; $i -lt 17; $i++) {
        if ($i % 2 -eq 0) {
            $liste_index_impair += $inverted_list[$i]
        } else {
            $liste_index_pair += $inverted_list[$i]
        }
        }

        $sum_pair = 0
        $sum_impair = 0

        ######### D?but de la partie du code qui g?re la liste des impairs #########

        #Partie du code qui g?re le cas o? un nombre est sup?rieur ? 10, dans ce cas on additionne les chiffres qui composent le nb.
        function AddDigits([int]$number) {
        $sum = 0
        while ($number -gt 0) {
            $sum += $number % 10
            $number = [Math]::Floor($number / 10)
        }
        return $sum
        }

        foreach ($i in $liste_index_impair) {
            $i = [int]$i
            $i = 2*$i
            if ($i -gt 9) {
                $i = AddDigits($i)
            
            }
            $sum_impair += $i
        
        }

        ######### Fin de la partie du code qui g?re la liste des impairs #########



        foreach ($i in $liste_index_pair) {
            $i = [int]$i
            $sum_pair += $i
        
        }

        function isValid() { 
                    $final_number = $sum_impair + $sum_pair
                    if ($final_number % 10 -eq 0) {
                        Write-Host("La carte est valide selon l'algorithme de Luhn")
                    }
                    else { 
                        Write-Host("La carte n'est pas valide selon l'algorithme de Luhn")
                    }
        }
    
        isValid

    }
    else {
        Write-Host ("Le nombre est mal saisi")
    }

}