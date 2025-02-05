
import http from 'k6/http';
import { check, sleep } from 'k6';
import { faker } from 'https://cdnjs.cloudflare.com/ajax/libs/Faker/3.1.0/faker.min.js';

export const options = {
  vus: 10,
  duration: '30s',
};

export default function () {
  const plate = faker.vehicle.vrm();
  const spot = faker.random.alphaNumeric(5);
  const apartment = faker.random.number({ min: 100, max: 999 });
  const block = faker.random.alpha();

  const payload = JSON.stringify({
    vehicle_plate: plate,
    spot_number: spot,
    apartment: apartment,
    block: block,
    user_id: 1, // Assuming a default user ID for testing
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post('http://localhost:5000/parking', payload, params);

  check(res, {
    'status is 201': (r) => r.status === 201,
  });

  sleep(1);
}