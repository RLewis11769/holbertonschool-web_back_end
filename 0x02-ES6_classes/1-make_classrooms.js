import ClassRoom from './0-classroom';

export default function initializeRooms() {
  // Return array of ClassRoom objects with specific sizes

  return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
}
