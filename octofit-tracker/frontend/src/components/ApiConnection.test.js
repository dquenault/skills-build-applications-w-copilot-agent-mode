import fetch from 'node-fetch';

describe('API Connection Tests', () => {
  const baseUrl = 'https://obscure-fortnight-qv64pq5xxr2xr9-8000.app.github.dev/api';
  const endpoints = ['users', 'workouts', 'teams', 'leaderboard', 'activities'];

  endpoints.forEach((endpoint) => {
    test(`should connect to ${endpoint} endpoint`, async () => {
      const response = await fetch(`${baseUrl}/${endpoint}`);
      expect(response.ok).toBe(true);
    });
  });
});
