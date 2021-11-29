<?php

namespace App;


class VeggieSub extends Sub {

    public function addPrimaryToppings()
    {
        var_dump('laying down the veggies');

        return $this;
    }

}
