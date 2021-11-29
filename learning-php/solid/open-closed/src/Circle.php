<?php

namespace Acme;

class Circle implements Shape {

    public $radius;

    public function __construct($radius)
    {
        $this->radius = $radius;
    }

    public function area()
    {
        return ($this->radius * 2) * 3.14;
    }
}
