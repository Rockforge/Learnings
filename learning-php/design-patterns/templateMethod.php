<?php

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
        var_dump('add some lettuce');

        return $this;
    }

    protected function addSauces()
    {
        var_dump('add some sauce');

        return $this;
    }

    /**
     * This abstract class is going to require
     * its subclass to require this method
     */
    protected abstract function addPrimaryToppings();

}

class VeggieSub extends Sub {

    public function addPrimaryToppings()
    {
        var_dump('add some veggies');

        return $this;
    }
}

class TurkeySub extends Sub {

    public function addPrimaryToppings()
    {
        var_dump('add some turkey');

        return $this;
    }
}


(new TurkeySub)->make();
(new VeggieSub)->make();
