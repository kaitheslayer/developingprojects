Link to website:

type: 
keanu "followed by anything:
example:
http://aditum.science/ce.php?q=keanu+i+ate+a+pie




// Php Code 

public function user_Keanu ($all, $sbar) {
    $all = str_replace('keanu', '', $all);
    $k = explode(" ", $all);
    $kn = str_word_count($all);
    $ka = Array();
    $a = "";
    $y= 3;
    array_push($ka, "Or did");
    if ($kn == 1) {
        $e = "Or did answer Keanu no found";
    
    }
   
    while ($y <= $kn) {
        array_push($ka, $k[$y]);
      
        $y = $y + 1;
    }
    array_push($ka, $k[2]);
    array_push($ka, $k[1]);
 
    if (!isset($e)) {
    $r = implode(" ", $ka);
		} else {
			$r = $e;
		}
    temp_def_stan1($r, "Or did Keanu algorithm by computed", "keanu algorithm", $sbar, "Michael and Kai");
    
  }
