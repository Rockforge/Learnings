<?php

namespace App;

abstract class Sub {

    public function make()
    {
        return $this
            ->layBread()
            ->addLettuce()
            ->addPrimaryToppings()
            ->addSauces();
    }

    protected function layBread()
    {
        var_dump('laying down the bread');

        return $this;
    }

    protected function addLettuce()
    {
        var_dump('laying down the lettuce');

        return $this;
    }

    protected function addSauces()
    {
        var_dump('laying down the sauce');

        return $this;
    }

    /**
     * This abstract class is going to require
     * its subclass to require this method
     */
    protected abstract function addPrimaryToppings();
}
