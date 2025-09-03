const passenger = {
  name: 'Manuel Bieh',
  class: 'economy',
};

const { name = 'Unknown Passenger' } = passenger;
const ticketClass = passenger.class || 'economy';

console.log(name, ticketClass);