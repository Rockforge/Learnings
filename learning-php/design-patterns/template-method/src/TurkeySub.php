<?php

namespace App;

class TurkeySub extends Sub {

    public function addPrimaryToppings()
    {
        var_dump('laying down the turkey');

        return $this;
    }

}
