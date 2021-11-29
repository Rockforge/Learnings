<?php

class CustomersRepository
{

    protected $customers;

    public function __construct(array $customers)
    {
        $this->customers = $customers;
    }

    public function all()
    {
        return $this->customers;
    }

    public function matchingSpecification($specification)
    {
        $matches = array_filter(
            $this->customers,
            function($customer) use ($specification) {
                return $specification->isSatisfiedBy($customer);
            }
        );

        return $matches;
    }

}
